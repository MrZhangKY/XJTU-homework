clear;
clc;
[f, p]=uigetfile('*.dat', '选择数据文件夹');   %读取数据文件夹
num = 5; %输入系数矩阵文件头的个数
name = strcat(p,f);
file = fopen(name, 'r');
head = fread(file, num, 'uint'); %读取二进制头文件
id = dec2hex(head(1)); %读取标识符
ver = dec2hex(head(2)); %读取版本号
n = head(3); %读取阶数
q = head(4); %上带宽
p = head(5); %下带宽

dist = 4*num;
fseek(file, dist, 'bof'); %把句柄值转向第六个元素开头处
[A, count] = fread(file, inf, 'float'); %读取二进制文件，获取系数矩阵
fclose(file);

%%对非压缩带状矩阵进行求解
if ver == '102'
    
    a = zeros(n,n); %系数矩阵a
    for i=1:n
        for j=1:n
            a(i,j)=A((i-1)*n+j); 
        end
    end
    
    b = zeros(n,1); %方程组右端系数b
    for i=1:n
        b(i) = A(n*n+i);
    end
    
    for k=1:n-1 %列主元高斯消去法
        m=k;
        for i=k+1:n %寻找主元
            if abs(a(m,k))<abs(a(i,k))
                m=i;
            end
        end
        if a(m,k)==0 %遇到条件终止
            disp('错误！')
            return
        end
        for j=1:n %交换元素位置得主元
            t = a(k,j);
            a(k,j) = a(m,j);
            a(m,j) = t;
            t = b(k);
            b(k) = b(m);
            b(m) = t;
        end
        for i=k+1:n %计算l（i，k）并将其放到a（i，k）中
            a(i,k) = a(i,k)/a(k,k);
            for j=k+1:n
                a(i,j) = a(i,j)-a(i,k)*a(k,j);
            end
            b(i) = b(i) - a(i,k)*b(k);
        end
    end
    
    x = zeros(n,1); %回代过程
    x(n) = b(n)/a(n,n);
    for k=n-1:-1:1
        x(k) = (b(k)-sum(a(k,k+1:n)*x(k+1:n)))/a(k,k);
    end
    
end

%%对压缩带状矩阵进行求解
if ver=='202' %高斯消去法
    m = p+q+1;
    
    a = zeros(n,m); %系数矩阵a
    for i=1:n
        for j=1:m
            a(i,j)=A((i-1)*m+j);
        end
    end
    
    b = zeros(n,1); %方程组右端系数b
    for i=1:1:n
        b(i)=A(n*m+i); 
    end
    
    for k=1:1:n-1 %消去
        if a(k,(p+1))==0
            disp('错误！');
            break;
        end
        st1 = n;
        if (k+p)<n
            st1 = k+p;
        end
        for i=(k+1):1:st1
            a(i,(k+p-i+1)) = a(i,(k+p-i+1))/a(k,(p+1));
            for j=(k+1):1:(k+p)
                a(i, (j+p-i+1)) = a(i, (j+p-i+1))-a(i, (k+p-i+1))*a(k, (j+p-k+1));
            end
            b(i) = b(i) - a(i, (k+p-i+1))*b(k);
        end
    end
    
    x = zeros(n,1); %回代
    x(n) = b(n)/a(n,p+1);
    sum = 0;
    for k=n-1:-1:1
        sum = b(k);
        st2 = n;
        if (k+p)<n
            st2 = k+q;
        end
        for j=(k+1):1:st2
            sum = sum-a(k, j+p-k+1)*x(j);
        end
        x(k) = sum/a(k,p+1);
        sum = 0;
    end
end

disp('方程组的解为:')
disp(x)