from parliament import Context, event
from datetime import datetime


@event
def main(context: Context):
    """
    Function template
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """

    # Print current date and time
    print("Current date and time:", datetime.now())

    # Print the entire cloud_event
    print("CloudEvent received:")
    print(context.cloud_event)

    # Optional: print specific fields
    print("CloudEvent data:")
    print(context.cloud_event.data)

    # The return value here will be applied as the data attribute
    # of a CloudEvent returned to the function invoker
    return context.cloud_event.data
