# A python script to monitor the system usage i.e CPU, Memory and Disk usage using psutil module and flask module for rendering.

from flask import Flask, render_template, redirect, jsonify
import psutil 

app = Flask(__name__) 

# Creating a route 
@app.route("/")
def index():
    # Getting the CPU usage
    cpu_percent = psutil.cpu_percent()

    # Getting the Memory usage
    mem_percent = psutil.virtual_memory().percent

    # Storing the message in a variable 
    Message = None

    # Checking the CPU usage 
    if cpu_percent > 80 or mem_percent > 80:
       Message = "High CPU or Memory Detected, scale up!"
       return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=Message)
    
    else:
        Message = "System is running smoothly"
        return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=Message)
    
@app.route("/github")
def github():
    return redirect("https://github.com/amandev-x/system-performance-monitoring")

@app.route("/health")
def health():
    try:
        cpu_percent = psutil.cpu_percent
        mem_percent = psutil.virtual_memory().percent

        # Consider the application healthy if both CPU and Memory are less than 90%
        is_healthy = cpu_percent < 90 and mem_percent < 90

        if is_healthy:
            return jsonify({
                "status": "healthy",
                "cpu_percent": cpu_percent,
                "mem_percent": mem_percent,
                "message": "Application is up and running"
            }), 200
        
        else:
            return jsonify({
                "status": "unhealthy",
                "cpu_percent": cpu_percent,
                "mem_percent": mem_percent,
                "message": "Application is running but experiencing high resource usage"
            }), 500
    except Exception as e:
        app.logger.error(f"Health check failed: {e}")

        return jsonify({
            "status": "unhealthy",
            "message": "Failed to retrieve system metrics"
        }), 500

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=5001)

