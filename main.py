import modal

app = modal.App('testappsquare')

@app.function()
def square(x: int) -> int:
    print('Running remotely...')
    return x ** 2


@app.local_entrypoint()
def main():
    print('The suare of 42 is: ', square.remote(42))

