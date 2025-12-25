# A python script to monitor the system usage i.e CPU, Memory and Disk usage using psutil module and flask module for rendering.

from flask import Flask, render_template, redirect
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

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=5001)

