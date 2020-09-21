def defang_ip_address(addr):
    defanged_address = ""
    for char in addr:
        if char == ".":
           defanged_address = defanged_address + "[.]"
        else:
            defanged_address = defanged_address + char
    return defanged_address
