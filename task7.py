def calculate_latency_bandwidth(log_file):
    # Initialize variables
    latency_sum = 0
    total_reads = 0
    total_requests = 0
    start_time = None
    end_time = None
    last_read_time = None
    bandwidth = 0

    # Open the log file
    with open(log_file, 'r') as f:
        # Skip the header line
        next(f)
        
        for line in f:
            # Parse each line of the log file
            timestamp, txn_type, data = line.strip().split('\t')

            # Convert timestamp to integer
            timestamp = int(timestamp)
            
            print("Transaction:", timestamp, txn_type, data)  # Debugging output

            if txn_type.startswith('Rd'):
                print("Read transaction detected")  # Debugging output
                # Calculate latency for read transactions
                if last_read_time is not None:
                    latency = timestamp - last_read_time
                    print("Latency:", latency)  # Debugging output
                    latency_sum += latency
                    total_reads += 1
                last_read_time = timestamp
            elif txn_type.startswith('Wr'):
                print("Write transaction detected")  # Debugging output
                # Calculate bandwidth for write transactions
                total_requests += 1

            # Calculate bandwidth for the entire log file
            end_time = timestamp
            if start_time is None:
                start_time = timestamp
            else:
                time_elapsed = end_time - start_time
                bandwidth = total_requests / time_elapsed

    # Calculate average latency
    if total_reads > 0:
        average_latency = latency_sum / total_reads
    else:
        average_latency = 0

    return average_latency, bandwidth

# Example usage
log_file = 'C:/Users/Admin/Desktop/GIRL HACKATHON/interface_log.txt'
average_latency, bandwidth = calculate_latency_bandwidth(log_file)
print("Average Latency:", average_latency)
print("Bandwidth:", bandwidth)

