#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>
#include<map>
#include <vector> 
#include<string>
using namespace std;
#define FOR(start,end) for(int i=start;i<end;i++)
#define lli long long int 
#define read(a) cin>>a;
#define readr(b,n) for(lli i=0;i<n;i++){cin>>b[i];}
#define printarr(arr,n) FOR(0,n){cout<<arr[i]<<" "; }cout<<endl;
const long int MOD = 1000000007;
struct node{
	int val;
	struct node* left;
	struct node* right;

};

struct node* new_node(){
	struct node* nw = new node();
	nw->left = NULL;
	nw->right = NULL;
	return nw;
}
void dfs(struct node* root){
	if(root == NULL){
		cout<<"NULL ";
		return;
	}
	cout<<root->val<<" ";
	if(root->left != NULL || root->right != NULL){	
		
		dfs(root->left);
		dfs(root->right);
	}
}
struct node* insert(struct node* root,int data){
	if(root == NULL){
		struct node* n = new_node();
		n->val = data;
		root = n;
		return n;
	}
	else{
		if(data>=root->val)
			root->right = insert(root->right,data);
		else
			root->left = insert(root->left,data);
		return root;
	}

}
void solve(){
	int n = 5;
	struct node* root = NULL;
	for (int i = 0; i < n; ++i)
	{
		int temp;
		cin>>temp;
		root = insert(root,temp);
	}
	dfs(root);
}
int main(){
	solve();
	return 0;
}
/* 
3
2
4
1
5
*/
