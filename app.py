from flask import Flask, request, render_template_string, render_template
import re
import subprocess
import os

app = Flask(__name__)

BLACKLIST = [
    'cat', 'flag', 'bash', 'sh', 'echo', '&&', '||', 
    '`', '$', '{', '}', '[', ']', 'grep', 'awk', 'sed',
    'more', 'less', 'curl', 'wget', 'nc', 'python', 'perl',
    'ruby', 'php', '>', '<', '>>', '<<', '*', '?', 'source',
    'eval', 'exec', 'system'
]

def check_command(cmd):
    cmd = cmd.lower()
    # Check for hex/octal encoding
    if any(x in cmd for x in ['\\x', '\\0']):
        return False
    # Check for blacklisted words, but only as whole words
    if any(f" {word} " in f" {cmd} " for word in BLACKLIST):
        return False
    # Allow more special chars for command injection
    if not re.match('^[a-zA-Z0-9\\s\\-\\/\\.\\_\\|\\;]+$', cmd):
        return False
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping', methods=['POST'])
def ping():
    target = request.form.get('target', '')
    
    if not target or len(target) > 100:
        return "Invalid input length", 400
        
    if not check_command(target):
        return "Nice try! But that's not allowed!", 403
    
    try:
        # Vulnerable command injection point with strict filtering
        cmd = f"timeout 5 ping -c 1 {target}"
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=5)
        return render_template_string("""
            <h3>Ping Results:</h3>
            <pre>{{ output.decode('utf-8') }}</pre>
            <a href="/">Back to home</a>
        """, output=output)
    except subprocess.TimeoutExpired:
        return "Command timed out", 408
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)