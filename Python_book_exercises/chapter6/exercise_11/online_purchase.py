"""Suppose you are purchasing something online on the Internet. At the website, you get
a 10% discount if you are a member. Additionally, you are also getting a discount of
5% on the item because its Father’s Day.
Write a function that takes as input the cost of the item that you are purchasing and
a Boolean variable indicating whether you are a member (or not), applies the discounts
appropriately, and returns the final discounted value of the item."""

def apply_discount():

    try:
        is_member = False
        item_cost_str = input("Input cost of item purchased: ")
        membership = input("Are you a member? [y/n]")

        membership = membership.lower()

        if membership == "y":
            is_member = True

        item_cost_float = float(item_cost_str)

    except ValueError as a:
        print(a)

    if is_member == False:
        percent = 5 / 100 * item_cost_float
        dicount_value = item_cost_float - percent
        return dicount_value
    elif is_member == True:
        percent = (15 / 100 * item_cost_float)
        dicount_value = item_cost_float - percent
        return dicount_value

def main():
    discount = apply_discount()
    print("Discounted value of item is: {}".format(discount))



if __name__ == '__main__':
    main()




