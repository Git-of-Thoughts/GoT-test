Based on the requirements and assumptions, we will need the following core classes and methods:

1. `RocketMQConsumer`: This is the main class that will handle the consumption of messages from RocketMQ. It will have the following methods:
   - `consume()`: This method will consume messages from RocketMQ.
   - `processMessage(Message message)`: This method will process the consumed message. It will check if the message has been processed before by checking its MessageId against a store of processed MessageIds. If the message has not been processed before, it will process the message and add its MessageId to the store of processed MessageIds.

2. `MessageStore`: This class will handle the storage of processed MessageIds. It will have the following methods:
   - `addMessageId(String messageId)`: This method will add a MessageId to the store.
   - `hasMessageId(String messageId)`: This method will check if a MessageId is in the store.

Now, let's implement these classes and methods in Java.

rocketmqconsumer.java
