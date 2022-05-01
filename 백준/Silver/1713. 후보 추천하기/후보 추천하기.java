
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Student implements Comparable<Student>{
	int num;
	int total;
	int time;
	public Student(int num, int total, int time) {
		super();
		this.num = num;
		this.total = total;
		this.time = time;
	}
	@Override
	public int compareTo(Student o) {
		if(this.total==o.total) {
			return this.time-o.time;
		}else if(this.total<o.total)return -1;
		else return 1;
	
	}
	
	
}

public class Main {
	static int n,m;
	static int[] students;
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		n=sc.nextInt();
		m=sc.nextInt();
		students=new int[101];
		ArrayList<Student> list=new ArrayList<>();
		for (int i = 0; i < m; i++) {
			int student=sc.nextInt();
			if(students[student]>0) {
				students[student]+=1;
				for (int j = 0; j <list.size(); j++) {
					if(list.get(j).num==student) {
						list.get(j).total+=1;
						break;
					}
				}
			}else {
				if(list.size()>=n) {
					Collections.sort(list);
					int num=list.get(0).num;
					students[num]=0;
					list.remove(0);
				}
				list.add(new Student(student,1,i));
				students[student]=1;
			}	
			
		}
		
		for (int i = 0; i <101; i++) {
			if(students[i]!=0) {
				System.out.print(i+" ");
			}
		}
		
		
	}
}