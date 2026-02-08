#simulate alarm based on certain performance values
#CONCEPT: If-else conditions

#Data:
cpu=80 #note tha it can handle other input like 'nil' or 'null'
memory=30 #this if 'nil' will trhow error
instance_state="Running"

print("--Starting Health check--")
if instance_state == "Running":
    #Running state
    if type(cpu) is int and cpu>=80:
        print(f"Critical CPU {cpu}")
    elif type(cpu) is int and 50<=cpu<80:
        print(f"Cpu warning {cpu}")
    elif type(cpu) is int and cpu<50:
        print(f"Cpu good {cpu}")
    else:
        print("Invalid CPU Detail")

    if memory>=80:
        print(f"Critical memory {memory}")
    elif 50<=memory<80:
        print(f"memory warning {memory}")
    elif memory<50:
        print(f"memory good {memory}")
    else:
        print("Invalid memory Detail")

elif instance_state == "stopped":
    print(f"The Instance has been stopped")
elif instance_state == "failed":
    print(f"The instance failed")
else:
    print("Error in data")
