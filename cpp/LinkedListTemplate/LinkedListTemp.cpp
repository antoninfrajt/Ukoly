<<<<<<< HEAD
#include <iostream>

using namespace std;

template <typename T>
struct LinkedListTemp
{
    int number;
    T val;
    LinkedListTemp* next;
    void print_node()
    {
        cout<<"Node: "<< number << " (Address: "<< this<<", val: "<< val <<", next: "<< next <<" )" <<endl;
    };
    void print_LL()
    {
        LinkedListTemp* current_node = this;
        while(current_node->next != NULL)
        {
            current_node->print_node();
            current_node = current_node->next;
        }
        current_node->print_node();
    };
    void pushback_value(T value)
    {
        int num = this->number;
        LinkedListTemp* new_node = new LinkedListTemp();
        LinkedListTemp* current_node = this;
        while (current_node->next != NULL)
        {
            num ++;
            current_node = current_node->next;
        }
        current_node->next = new_node;
        new_node->val = value;
        new_node->next = NULL;
        new_node->number = current_node->number+1;
    };
    void insert_value(T value, int idx)
    {
        LinkedListTemp* current_node = this;
        for (int i = 0;i<idx;i++)
        {
            current_node = current_node->next;
        }
        current_node->val = value;
    };
    LinkedListTemp* operator[](int idx)
    {
        LinkedListTemp* current_node = this;
        for (int i=0;i<idx;i++)
        {
            if(current_node->next != NULL) current_node = current_node->next;
            else cout<<"Index out of range";
        }
        return current_node;
    };
    void delete_node(int idx)
    {
        LinkedListTemp* current_node = this;
        LinkedListTemp* next_node = NULL;
        // Chabý pokus o mazání prvního elementu, jen nevím jak změnit header
        if (idx == 0)
        {
            delete current_node;
        }
        else 
        {
            for (int i=0;i<idx-1;i++)
            {
                current_node = current_node->next;
            }
            next_node = current_node->next;
            if (next_node->next == NULL) 
            {
                delete next_node;
                current_node->next = NULL;
            }
            else 
            {
                current_node->next = next_node->next;
                delete next_node;
                int num = current_node->number;
                while(current_node->next != NULL)
                {
                    current_node = current_node->next;
                    current_node->number = num+1;
                    num ++;
                }
            }
        }
    };

};
 
int main()
{
    LinkedListTemp <int> LL;
    LL.val = 0;
    LL.next = NULL;
    LL.number = 0;

    LL.pushback_value(1);
    LL.pushback_value(2);
    LL.pushback_value(3);

    LL.print_LL();
    LL[1]->print_node();

    LL.insert_value(4,2);
    LL.delete_node(0);
    LL.print_LL();	
}
=======
#include <iostream>

using namespace std;

template <typename T>
struct LinkedListTemp
{
    int number;
    T val;
    LinkedListTemp* next;
    void print_node()
    {
        cout<<"Node: "<< number << " (Address: "<< this<<", val: "<< val <<", next: "<< next <<" )" <<endl;
    };
    void print_LL()
    {
        LinkedListTemp* current_node = this;
        while(current_node->next != NULL)
        {
            current_node->print_node();
            current_node = current_node->next;
        }
        current_node->print_node();
    };
    void pushback_value(T value)
    {
        int num = this->number;
        LinkedListTemp* new_node = new LinkedListTemp();
        LinkedListTemp* current_node = this;
        while (current_node->next != NULL)
        {
            num ++;
            current_node = current_node->next;
        }
        current_node->next = new_node;
        new_node->val = value;
        new_node->next = NULL;
        new_node->number = current_node->number+1;
    };
    void insert_value(T value, int idx)
    {
        LinkedListTemp* current_node = this;
        for (int i = 0;i<idx;i++)
        {
            current_node = current_node->next;
        }
        current_node->val = value;
    };
    LinkedListTemp* operator[](int idx)
    {
        LinkedListTemp* current_node = this;
        for (int i=0;i<idx;i++)
        {
            if(current_node->next != NULL) current_node = current_node->next;
            else cout<<"Index out of range";
        }
        return current_node;
    };
    void delete_node(int idx)
    {
        LinkedListTemp* current_node = this;
        LinkedListTemp* next_node = NULL;
        // Chabý pokus o mazání prvního elementu, jen nevím jak změnit header
        if (idx == 0)
        {
            delete current_node;
        }
        else 
        {
            for (int i=0;i<idx-1;i++)
            {
                current_node = current_node->next;
            }
            next_node = current_node->next;
            if (next_node->next == NULL) 
            {
                delete next_node;
                current_node->next = NULL;
            }
            else 
            {
                current_node->next = next_node->next;
                delete next_node;
                int num = current_node->number;
                while(current_node->next != NULL)
                {
                    current_node = current_node->next;
                    current_node->number = num+1;
                    num ++;
                }
            }
        }
    };

};
 
int main()
{
    LinkedListTemp <int> LL;
    LL.val = 0;
    LL.next = NULL;
    LL.number = 0;

    LL.pushback_value(1);
    LL.pushback_value(2);
    LL.pushback_value(3);

    LL.print_LL();
    LL[1]->print_node();

    LL.insert_value(4,2);
    LL.delete_node(0);
    LL.print_LL();	
}
>>>>>>> 5416915f6e236b2c4f9e3ce51dee2d4b630d547c
