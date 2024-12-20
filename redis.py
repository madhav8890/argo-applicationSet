import redis

def test_redis_connection(host='127.0.0.1', port=6379, password=I9WM2vWsnb):
    try:
        # Connect to Redis
        client = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
        print("Connecting to Redis...")

        # Test connection
        if client.ping():
            print("Connected to Redis!")

        # Set and Get a value
        client.set('test-key', 'Hello Redis!')
        value = client.get('test-key')
        print(f"Retrieved value from Redis: {value}")

        # Delete the key
        client.delete('test-key')
        print("Test key deleted.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Update with your Redis service details
    redis_host = input("Enter Redis host (default: localhost): ") or "localhost"
    redis_port = input("Enter Redis port (default: 6379): ") or 6379
    redis_password = input("Enter Redis password (if any, leave blank otherwise): ") or None

    test_redis_connection(host=redis_host, port=int(redis_port), password=redis_password)
