import Pyro4
# Connect to the remote object
def main():
    server = Pyro4.Proxy("PYRO:string.concatenator@localhost:9090")
    str1 = input("Enter the first string:")
    str2 = input("Enter the second string:")
    try:
        result = server.concatenate(str1, str2)
        print(f"Concatenated String: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()

import Pyro4
# Define the remote object
@Pyro4.expose
class StringConcatenator:
    def concatenate(self, str1, str2):
        return str1 + str2
    
# Register the remote object with the Pyro4 daemon
def main():
    Pyro4.Daemon.serveSimple({
        StringConcatenator: "string.concatenator"
        },
        host="localhost",
        port=9090,
        ns=False
)
print("StringConcatenator server is running...")

if __name__ == "__main__":
    main()
