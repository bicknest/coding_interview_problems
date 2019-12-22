# Approach

The solution is quite simple. Relying on the fact that addition is commutative (a + b == b + a) we do not need to calculate shorter + longer and longer + shorter.

Futhermore there are only two plank sizes and they must be different.

So:

Start at the smallest length (all short planks) possible and generate the next lengths by replacing (one at a time) shorter planks with longer planks.

We know that the bounds are (all short planks) -> (all long planks) and with each plank replacement the overall length will increase.

This means that we will always generate a unique value (efficient because we aren't doing any extra work) and due to the commuatative property of addition we know we are generating the entire set.

This algorithm will run in O(k + 1) time and will take O(k + 1) space.
