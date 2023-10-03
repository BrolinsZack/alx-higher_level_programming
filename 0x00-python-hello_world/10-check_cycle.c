#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly linked list 
                 has a cycle in it.
 * @list: A singly-linked list.
 *
 * Return: 0 if no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *car, *truck;

	if (list == NULL || list->next == NULL)
		return (0);

	car = list->next;
	truck = list->next->next;

	while (car && truck && truck->next)
	{
		if (car == truck)
			return (1);

		car = car->next;
		truck = truck>next->next;
	}

	return (0);
}
