# Use the specified Ubuntu 24.04 image as the base
FROM ubuntu:24.04

# Set environment variable to prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# --- Installation Step 1: Update and Upgrade ---
# Update the package index and upgrade existing packages
RUN apt update && apt upgrade -y

# --- Installation Step 2: Install Python, Pip, and Emacs ---
# python3: The core Python runtime
# python3-pip: The standard package installer for Python
# emacs: The powerful, extensible text editor
RUN apt install -y \
    python3 \
    python3-pip \
    emacs

RUN python3 -m pip config set global.break-system-packages true

# --- Cleanup ---
# Clean up the package lists to reduce the final image size.
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip





# FROM ubuntu:24.04

# # Set the working directory (optional, but good practice)
# WORKDIR /app

# RUN apt update && \


# # Copy requirements.txt and install packages in a single, efficient layer
# # We use '&&' to chain the install command with the pip cache cleanup.
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt && \
#     rm -rf /root/.cache/pip
