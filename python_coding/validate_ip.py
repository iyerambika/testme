def is_valid_ip_port(ip_str):
    ip_parts = ip_str.split(':')
    if len(ip_parts) != 2:
        return False

    try:
        port = int(ip_parts[1])
        if port < 1 or port > 65535:
            return False
    except ValueError:
        return False

    ip_address = ip_parts[0].split('.')
    for elem in ip_address:
        try:
            int_elem = int(elem)
            if int_elem < 0 or int_elem > 255:
                return False
        except ValueError:
            return False
    return True

print(is_valid_ip_port('256.168.0.1:8080'))


