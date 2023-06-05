#ifndef EVANS_LISTS_H
#define EVANS_LISTS_H

#include <stdlib.h>

/**
 * struct evans_list_s - singly linked list
 * @num: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Evans project
 */
typedef struct evans_list_s
{
    int num;
    struct evans_list_s *next;
} evans_list_t;

size_t print_evans_list(const evans_list_t *h);
evans_list_t *add_node_evans(evans_list_t **head, const int num);
void free_evans_list(evans_list_t *head);
int check_evans_cycle(evans_list_t *list);

#endif /* EVANS_LISTS_H */
