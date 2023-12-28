#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
  int data;
  struct Node *left;
  struct Node *right;
}Node;

Node *create_node(int data){
  Node* newNode = (Node*) malloc(sizeof(Node));
  newNode->data = data;
  newNode->left = NULL;
  newNode->right = NULL;
  return newNode;
}

Node* insert(Node* node, int data){
  if(node == NULL) return create_node(data);
  if(node->data > data) node->left = insert(node->left, data);
  else node->right = insert(node->right, data);
  return node;
}

Node* minValue(Node* node){
  Node* current = node;
  while(current && current->left != NULL){
    current = current->left;
  }
  return current;
}

void swap(Node* node, int old, int new){
  Node* current = node;
  while(current != NULL){
    if(current->data == old){
      current->data = new;
      return;
    }
    else if(current->data > old) current = current->right;
    else current = current->left;
  }
}

Node* delete(Node* node, int data){
  if(node == NULL) return node;
  if(node->data > data){
    node->left = delete(node->left, data);
  }
  else if(node->data < data){
    node->right = delete(node->right, data);
  }
  else{
    if(node->left == NULL){
      Node* temp = node->right;
      free(node);
      return temp;
    }
    else if(node->right == NULL){
      Node* temp = node->left;
      free(node);
      return temp;
    }
    else{
      Node* temp = minValue(node->right);
      node->data = temp->data;
      node->right = delete(node->right, temp->data);
    }
    return node;
  }
}

void inorder(Node* node){
  if(node == NULL) return;
  inorder(node->left);
  printf("%d -> ", node->data);
  inorder(node->right);
}

void preorder(Node* node){
  if(node == NULL) return;
  printf("%d -> ", node->data);
  preorder(node->left);
  preorder(node->right);
}

void postorder(Node* node){
  if(node == NULL) return;
  postorder(node->left);
  postorder(node->right);
  printf("%d -> ", node->data);
}

int main(){
  Node* root = create_node(10);
  insert(root, 15);
  insert(root, 16);
  insert(root, 14);
  insert(root, 5);
  insert(root, 4);
  insert(root, 8);
  insert(root, 9);
  insert(root, 6);

  Node* min = minValue(root);
  printf("minimum data: %d\n", min->data); // 4

  printf("pre-order traversal: \n");
  preorder(root); // 10 -> 5 -> 4 -> 8 -> 6 -> 9 -> 15 -> 14 -> 16 ->
  printf("\n");
  printf("in-order traversal: \n");
  inorder(root); // 4 -> 5 -> 6 -> 8 -> 9 -> 10 -> 14 -> 15 -> 16 ->
  printf("\n");
  printf("post-order traversal: \n");
  postorder(root); // 4 -> 6 -> 9 -> 8 -> 5 -> 14 -> 16 -> 15 -> 10 ->
  

  return 0;
} 