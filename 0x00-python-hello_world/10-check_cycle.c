#include "lists.h"

/**
 * check_cycle - Function that checks if a singly linked list 
                 contains a cycle in it.
 * @list: A singly-linked list.
 *
 * Return: 0 if no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *tea, *coffee;

	if (list == NULL || list->next == NULL)
		return (0);

	canoe = list->next;
	yatch = list->next->next;

	while (tea && coffee && coffee->next)
	{
		if (tea == coffee)
			return (1);

		tea = tea->next;
		coffee = coffee->next->next;
	}

	return (0);
}
