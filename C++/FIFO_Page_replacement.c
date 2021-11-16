#include<limits.h>
#include<stdio.h>
#include<stdlib.h>
#define MAX(x,y) (((x)>(y)) ? (x):(y))

int top =0;
int pg_fault=0;

//fifo takes care of the frames
struct fifo{
	int pn;
};

//time takes care of the
//time the page has been in stack
struct time{
	int in_stack;
};

//Displays the current stack(frames)
void disp(struct fifo fif_stk[], struct time page_time[],int n)
{
	printf("CurrStack View :");
	for(int i=0;i<n;i++){
		printf("%d\t",fif_stk[i].pn);
	}
	printf("\n");
	printf("Each Page time :");
	for(int i=0;i<n;i++)
	printf("%d\t",page_time[i].in_stack);
	printf("\n");
}

//returns the index having the oldest page
int longest_index_calculator(struct time page_time[],int n)
{
	int maximum_time = INT_MIN;
	int index;
	for(int i=0;i<n;i++)
	{
		int a = maximum_time;
		maximum_time = MAX(page_time[i].in_stack,maximum_time);
		if(a != maximum_time)
			index = i;

	}
	return index;
}

//Replaces the page on the basis of age of the page
void page_replace(struct fifo fif_stk[], struct time page_time[], int n,int pg_no)
{
	int flag =0;
	int i =0;
	while(i<n)
	{
		if(fif_stk[i].pn==pg_no)
		{
			page_time[i].in_stack++;
			flag =1;
			break;
		}
		i++;
	}
	if(flag==0)
	{
		int longest_indexed=longest_index_calculator(page_time,n);
		fif_stk[longest_indexed].pn = pg_no;
		page_time[longest_indexed].in_stack=1;
		pg_fault++;
	}
	else
		flag =0;
	disp(fif_stk,page_time,n);
}

//Insertion is called to insert new pages to the frames
void insertion(struct fifo fif_stk[],struct time page_time[],int n)
{
	int num;
	int flag =0;
	scanf("%d",&num);
	
	for(int i=0;i<n;i++)// Incrementing the already existing frames
	{
		if(fif_stk[i].pn != num)
		{
			page_time[i].in_stack++;
		}
	}
	//Checks if the stack is full
	if(top==0||top<=n-1){
		if(top==0){
			fif_stk[top].pn=num;
			page_time[top].in_stack=1;
			top++;
			pg_fault++;
		}
		else
		{
			int i=0;
			while(i<n){
				if(fif_stk[i].pn==num)
				{
					flag = 1;
					page_time[i].in_stack++;
					break;
				}
				i++;
			}
			if(flag==0){
				fif_stk[top].pn=num;
				page_time[top].in_stack=1;
				top++;
				pg_fault++;
			}
			else
				flag=0;

		}
		disp(fif_stk,page_time,n);
	}

	//When the stack is full
	//Uses the page replacement algorithm
	else if(top > n-1)
		page_replace(fif_stk,page_time,n,num);

}


int main()
{
	int n, tot_pg;
	printf("Enter no. of frames :");
	scanf("%d",&n);
	
	//Array of structured fifo
	struct fifo fif_stk[n];
	for(int i=0;i<n;i++)
		fif_stk[i].pn=-1;
	
	//Array of structure for time
	struct time page_time[n];
	for(int i=0;i<n;i++)
		page_time[i].in_stack=0;

	printf("Enter the number of pages :");
	scanf("%d",&tot_pg);

	for(int i=0;i<tot_pg;i++)
	insertion(fif_stk,page_time,n);
	
	disp(fif_stk,page_time,n);
	
	printf("Page fault: %d\n",pg_fault );
	return 0;

}
