#include <stdio.h>

void swap(int* a, int* b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

void insert(int arr[], int *size, int key){
  int i = *size;
  arr[i] = key;
  (*size)++;
  while(i != 0 && arr[(i-1) / 2] > arr[i]){
    swap(&arr[(i-1) / 2], &arr[i]);
    i = (i-1) / 2;
  }
}

void heapify(int arr[], int size, int i){
  int largest = i;
  int left = 2 * i + 1;
  int right = 2 * i + 2;
  if((left < size) && (arr[left] < arr[largest])){
    largest = left;
  }
  if((right < size) && (arr[right] < arr[largest])){
    largest = right;
  }
  if(largest != i){
    swap(&arr[i], &arr[largest]);
    heapify(arr, size, largest);
  }
}

void heapSort(int arr[], int size){
  // making a heap out of a unsorted array
  int largest = size / 2 - 1;
  for(int i = largest; i >= 0; i--){
    heapify(arr, size, i);
  }
  // sorting the array
  for(int i = size - 1; i >= 0; i--){
    swap(&arr[0], &arr[i]);
    heapify(arr, i, 0);
  }


}

void deleteRoot(int arr[], int* size){
  int last_element = arr[(*size)-1];
  arr[0] = last_element;
  (*size)--;
  heapify(arr, *size, 0);
}

void printArr(int arr[], int size){
  for(int i = 0; i < size; i++){
    printf("%d -> ",arr[i]);
  }
}

#define CAPACITY 10
int main(){
  int arr[CAPACITY];
  int arr1[CAPACITY] = {50, 40, 70, 20, 10, 5, 35, 60, 1, 65};
  int size = 0;
  for(int i = 0; i < CAPACITY; i++){
    insert(arr, &size, arr1[i]);
  }

  deleteRoot(arr, &size); // 5 -> 20 -> 10 -> 50 -> 40 -> 70 -> 35 -> 60 -> 65 ->
  deleteRoot(arr, &size); // 10 -> 20 -> 35 -> 50 -> 40 -> 70 -> 65 -> 60 ->
  deleteRoot(arr, &size); // 20 -> 40 -> 35 -> 50 -> 60 -> 70 -> 65 ->
  deleteRoot(arr, &size); // 35 -> 40 -> 65 -> 50 -> 60 -> 70 ->

  printArr(arr, size);
  printf("\n");

  int size1 = sizeof(arr1) / sizeof(int);
  heapSort(arr1, size1);
  printArr(arr1, size1); // 70 -> 65 -> 60 -> 50 -> 40 -> 35 -> 20 -> 10 -> 5 -> 1 ->
}