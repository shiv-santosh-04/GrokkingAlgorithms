def tower_of_hanoi(n, source, target, aux):

    #Base case
    if n == 1:
        print(f"Move disk 1 {source} to {target}")
        return

    #recursive case
    #step-1 move n-1 disks from source to aux
    tower_of_hanoi(n-1,source,aux,target)
    # step-2 move largest disk from source to target
    print(f"Move disk {n} {source} to {target}")
    #moce remaining n-1 disks from aux to target
    tower_of_hanoi(n-1,aux,target,source)

tower_of_hanoi(3,'A','C','B')
