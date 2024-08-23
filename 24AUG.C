vector<int> leftView(Node *root)
{
   if(root==nullptr){
       
       return {};
   }
   queue<Node*>q;
   
   q.push(root);
  
     vector<int>res;
   while(!q.empty()){
     int n=q.size();
     int cnt=0;
     
     for(int i=0;i<n;i++){
         Node* temp=q.front();
         
         if(cnt==0){
 res.push_back(temp->data);
          cnt++;
         }   
         q.pop();
       
         if(temp->left){
            q.push(temp->left);
            
         }
         if(temp->right){
             q.push(temp->right);
         }
     }
   }
      return res;
}
