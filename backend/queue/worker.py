import redis

r = redis.Redis(host="redis", port=6379)

def enqueue(job):
    r.lpush("jobs", job)

def worker():
    while True:
        job = r.rpop("jobs")
        if job:
            print("processing:", job)
