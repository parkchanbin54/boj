import sys
import copy

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    pm = [1,-1,10]
    def back_tracking(arr,x,l,cnt):
        if cnt == l:
            if sum(pq) == 0:
                ans.append(copy.deepcopy(pq))
            return

        for i in range(x,l):
            for p in pm:
                if p == 10:
                    tt = pq.pop()
                    if tt > 0:
                        pq.append((tt*10+arr[i]))
                    else:
                        pq.append((tt*10-arr[i]))
                    back_tracking(arr,i+1,l,cnt+1)
                else:
                    pq.append((p*arr[i]))
                    back_tracking(arr,i+1,l,cnt+1)
                    pq.pop()


    for k in range(n):

        tmp = int(input())
        arr = [i for i in range(1,tmp+1)]
        pq = [arr[0]]
        ans = []
        back_tracking(arr,1,tmp,1)
        ans_tmp = []
        ans.sort()
        for aa in sorted(ans):
            a_tmp =""
            for a in aa:
                s_tmp = str(abs(a))
                if len(str(abs(a))) > 1:
                    s_tmp = str(" ".join(list(str(abs(a)))))
                if a > 0:
                    a_tmp += "+"+s_tmp
                else:
                    a_tmp += "-"+s_tmp
            ans_tmp.append(a_tmp[1:])

        for ans_t in sorted(ans_tmp):
            print(ans_t)

        print("")