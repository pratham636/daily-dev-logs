    
    #include<stdio.h>
#include<stdlib.h>
struct Node
{
    int data;
    struct Node *next;
};
void linktra(struct Node *ptr)
{
    while (ptr!=NULL)
    {
        printf("%d \n",ptr->data);
        ptr=ptr->next;
    }
}
struct Node * insert_end(struct Node *head,struct Node *head1,struct Node *head2)
{
    struct Node * ptr = (struct Node *) malloc(sizeof(struct Node));
    ptr->data=NULL;
    struct Node* p;
        struct Node* q;
            struct Node* r;
    p=head;
    q=head1;
    r=head2;

    while (p->next!=NULL||r->next!=NULL||q->next!=NULL)
    {
        if (p->data>=q->data&&p->data>=r->data){
                p->next=ptr;
                ptr->next=NULL;
        }
        if (q->data>=r->data){
                q->next=ptr;
                ptr->next=NULL;
        }
        else{
                r->next=ptr;
                ptr->next=NULL;
        }
        p=p->next; 
    }
    p->next=ptr;
    ptr->next=NULL;
    return head;
}
int main()
{
    struct Node *head;
    struct Node *first;
    struct Node *second;
    struct Node *third;
    head=(struct Node *) malloc(sizeof(struct Node));
    first=(struct Node *) malloc(sizeof(struct Node));
    second=(struct Node *) malloc(sizeof(struct Node));
    third=(struct Node *) malloc(sizeof(struct Node));
    head->data=12;
    head->next=first;
    first->data=543;
    first->next=second;
    second->data=43;
    second->next=third;
    third->data=45;
    third->next=NULL;
    linktra(head);
    printf("\n\n");
    //insert at end
    head=insert_end(head,head1,head2);
    linktra(head);
    return 0;
}