provider "docker" {
  source = "kreuzwerker/docker"  # Specify the correct source for the Docker provider
  host   = "unix:///var/run/docker.sock"  # Local Docker setup
}

resource "docker_container" "travel_backend" {
  image = "travel_backend"  # Your Docker image name
  name  = "travel_backend_container"
  
  ports {
    internal = 5000
    external = 5000
  }

  volumes {
    host_path      = "/path/to/your/app"  # Update this to the correct path of your app directory
    container_path = "/app"
  }

  restart = "unless-stopped"
}
