clear;
clc;
[f, p]=uigetfile('*.dat', 'ѡ�������ļ���');   %��ȡ�����ļ���
num = 5; %����ϵ�������ļ�ͷ�ĸ���
name = strcat(p,f);
file = fopen(name, 'r');
head = fread(file, num, 'uint'); %��ȡ������ͷ�ļ�
id = dec2hex(head(1)); %��ȡ��ʶ��
ver = dec2hex(head(2)); %��ȡ�汾��
n = head(3); %��ȡ����
q = head(4); %�ϴ���
p = head(5); %�´���

dist = 4*num;
fseek(file, dist, 'bof'); %�Ѿ��ֵת�������Ԫ�ؿ�ͷ��
[A, count] = fread(file, inf, 'float'); %��ȡ�������ļ�����ȡϵ������
fclose(file);

%%�Է�ѹ����״����������
if ver == '102'
    
    a = zeros(n,n); %ϵ������a
    for i=1:n
        for j=1:n
            a(i,j)=A((i-1)*n+j); 
        end
    end
    
    b = zeros(n,1); %�������Ҷ�ϵ��b
    for i=1:n
        b(i) = A(n*n+i);
    end
    
    for k=1:n-1 %����Ԫ��˹��ȥ��
        m=k;
        for i=k+1:n %Ѱ����Ԫ
            if abs(a(m,k))<abs(a(i,k))
                m=i;
            end
        end
        if a(m,k)==0 %����������ֹ
            disp('����')
            return
        end
        for j=1:n %����Ԫ��λ�õ���Ԫ
            t = a(k,j);
            a(k,j) = a(m,j);
            a(m,j) = t;
            t = b(k);
            b(k) = b(m);
            b(m) = t;
        end
        for i=k+1:n %����l��i��k��������ŵ�a��i��k����
            a(i,k) = a(i,k)/a(k,k);
            for j=k+1:n
                a(i,j) = a(i,j)-a(i,k)*a(k,j);
            end
            b(i) = b(i) - a(i,k)*b(k);
        end
    end
    
    x = zeros(n,1); %�ش�����
    x(n) = b(n)/a(n,n);
    for k=n-1:-1:1
        x(k) = (b(k)-sum(a(k,k+1:n)*x(k+1:n)))/a(k,k);
    end
    
end

%%��ѹ����״����������
if ver=='202' %��˹��ȥ��
    m = p+q+1;
    
    a = zeros(n,m); %ϵ������a
    for i=1:n
        for j=1:m
            a(i,j)=A((i-1)*m+j);
        end
    end
    
    b = zeros(n,1); %�������Ҷ�ϵ��b
    for i=1:1:n
        b(i)=A(n*m+i); 
    end
    
    for k=1:1:n-1 %��ȥ
        if a(k,(p+1))==0
            disp('����');
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
    
    x = zeros(n,1); %�ش�
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

disp('������Ľ�Ϊ:')
disp(x)