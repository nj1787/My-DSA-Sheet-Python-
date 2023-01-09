def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print('Move Disk From {} to {}'.format(source, destination))
        return
    tower_of_hanoi(n - 1, source, destination, helper)
    print('Move Disk from {} to {}'.format(source, destination))
    tower_of_hanoi(n - 1, helper, source, destination)


# Main
disks = 1
tower_of_hanoi(disks, 'Source', 'Helper', 'Destination')



#---------------------------------------------------------SAMPLE I/O-------------------------------------------------------------------------------------#

Move Disk From Source to Destination   #Output for 1 disk

Move Disk From Source to Helper        #Output for 2 disks
Move Disk from Source to Destination
Move Disk From Helper to Destination

Move Disk From Source to Destination   #Output for 3 disks
Move Disk from Source to Helper
Move Disk From Destination to Helper
Move Disk from Source to Destination
Move Disk From Helper to Source
Move Disk from Helper to Destination
Move Disk From Source to Destination

