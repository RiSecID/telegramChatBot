# We're using Alpine Latest
FROM heinzdf/oubnew:latest
 
# Clone repo and prepare working directory
RUN git clone https://github.com/RiSecID/telegramChatBot /telegramChatBot
RUN chmod 777 /telegramChatBot
WORKDIR /telegramChatBot
 
# Install requirements
CMD ["python3","-m","bot.py"]
