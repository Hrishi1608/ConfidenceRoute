import docker

client = docker.from_env()

def run_code_sandboxed(code: str) -> str:
    try:
        output = client.containers.run(
            "python:3.11-slim",
            f'python -c "{code}"',
            remove=True,
            network_disabled=True,
            mem_limit="128m"
        )
        return output.decode()
    except Exception as e:
        return f"Error: {e}"
