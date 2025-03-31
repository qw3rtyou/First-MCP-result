FROM python:3.9-slim

WORKDIR /app

# Install required packages
RUN apt-get update && apt-get install -y \
    iputils-ping \
    xxd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Create non-root user
RUN useradd -m -r -s /bin/bash ctfuser
RUN chown -R ctfuser:ctfuser /app

# Create and set permissions for the flag
RUN echo "MCP{C0mm4nd_1nj3ct10n_M4st3r_Y0u_B34t_Th3_F1lt3r5}" > /flag.txt
RUN chmod 444 /flag.txt
RUN chown root:root /flag.txt

# Set capabilities for ping and other binaries
RUN setcap cap_net_raw+ep /usr/bin/ping

USER ctfuser

EXPOSE 5555

CMD ["python", "app.py"]