* Problem Definition

You write a messaging app that uses a mesh approach to get messages from one user to another.
Because coverage can be flaky in places, your app sends messages via the phones of nearby users,
passing each message along from one phone to the next until it reaches the intended recipient.

You want to write an algorithm that will take the optimal route from sender to recipient.

SO: Given information about the active users on the network, find the shortest route for a message from one ( the sender) to another (the recipient)

Input: a graph that looks somethinglike this:

network = {
    'Mike', : ['William', 'Jayden', 'Omar'],
    'William': ['Mike', 'Naomi'],
    'Naomi': ['Jayden', 'William'],
    'Jayden': ['Amelia', 'Ren', 'Naomi'],
    ...etc.
};

Output:
An array of users that make up the most efficient route from sender to recipient
