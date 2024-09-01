# Use the official Rasa SDK image as the base image
FROM rasa/rasa:latest

# Set environment variables
ENV RASA_HOME=/app
WORKDIR $RASA_HOME

# Copy the Rasa project files into the Docker container
COPY . $RASA_HOME

# Install custom actions requirements
# RUN pip install -r actions/requirements.txt

# Expose the default Rasa port
EXPOSE 5005

# Run Rasa server
CMD ["run", "--enable-api", "--cors", "*", "--debug"]