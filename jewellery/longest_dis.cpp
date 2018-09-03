#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

vector<int> g[10005];
int distance=0;
int bfs(int s)
{
	queue<int>q;
	q.push(s);
	int dis[n+1];
	for(int i=0;i<n+1;i++)
	{
		d[i]=-1;
	}
	d[s]=0;
	while(!q.empty())
	{
		x=q.front();
		q.pop();
		for(int i=0;i<g[x].size();i++)
		{
			if(dis[g[x][i]]==-1)
			{
				dis[g[x][i]]=dis[x]+1;
				q.push(g[x][i]);
			}
		}
	}
	int max=0;
	int id=0;
	for(int i=1;i<=n;i++)
	{
		if(dis[i]>max)
		{
			max=dis[i];
			id=i;
		}
	}
	distance=max;
	return id;
}
int main()
{
	int n;cin>>n;
	//vector<int> g[n+1];
	for(int i=0;i<n-1;i++)
	{
		int x,y;cin>>x>>y;
		g[x].push_back(y);
		g[y].push_back(x);
	}
	int a=bfs(1);
	int b=bfs(a);
	cout<<distance<<endl;
	return 0;
}