#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Injects a figure to a sorted singly-linked list.
 * @head: Pointer to linked list.
 * @num: The figure to ne injected.
 *
 * Return: Error or fails (0)
 * Otherwise - a pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int num)

{
	listint_t *current = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = num;

	if (current == NULL || current->n >= num)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	while (current && current->next && current->next->n < num)
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
