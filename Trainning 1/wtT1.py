f=open('D:\\Desktop\\randlist.txt')
s=f.read()      #��ȡ�ļ�
global list_all
global list_to_statistic
def tran_s_to_list(s):
        list_all=[]
        z={}
        l=len(s)        #�õ����ȣ�����
        for x in xrange(0,l):
                if not s[x] in list_all:
                        list_all.append(s[x])#��x����list�У�����һ�γ��֣�׷�ӵ�list_all��
                #print list_all
        for x in list_all:
            list_count=s.count(x)#ͳ���ַ����ֵĴ���
            #print(x)
            #print list_count
            z.update({x:list_count})
        #print z
        sorted_z = sorted(z.iteritems(), key=lambda x : x[1])#�������
        print sorted_z
        #print "Value : %s" % sorted_z.values()

tran_s_to_list(s)

