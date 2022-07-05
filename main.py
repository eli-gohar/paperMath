# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def withSets():
    T = 0  ## time_slot
    V = {1, 2, 3, 4}  ## set_of_cp

    W = {(1, 2), (1, 3), (1, 4),
         (2, 3), (2, 4),
         (3, 4)}  ## set_of_lc

    Rt = {1, 2}  ## set_of_nsr at time_slot T-1

    Sr = {
        frozenset({(1, 5.0), (1, 2.0)}),
        frozenset({(3, 10.0), (3, 4.0)})}  ## set_of_vnf that belong to r

    Lr = {}  ## set_of_virtual_links

    for T in range(1, 6):
        print(T)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    T = 3  ## time_slot
    V = ["Stavanger", "Oslo", "Bergen"]  ## set_of_cp

    ## set_of_lc
    W = [(cp, cp_2) for _, cp in enumerate(V) for _, cp_2 in enumerate(V) if cp != cp_2]
    print(W)

    R_t = [None, ["NSR_a", "NSR_b"], None]  ## set_of_nsr at time_slot t = 0, 1, and 2

    Sr = [
        ["vnf_alpha", "vnf_beta"],
        ["vnf_gamma", "vnf_point"]]  ## set_of_vnfs that belong to r

    Lr = []  ## set_of_virtual_links that belong to r

    for t in range(0, T):
        print("time_slot (t-1)= ", t)
        print("R_({})= {}".format(t, R_t[t]))
        if R_t[t] is not None:
            for r in range(len(R_t[t])):
                print("r= ", R_t[t][r])
                input()
