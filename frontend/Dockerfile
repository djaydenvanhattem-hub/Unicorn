FROM node:20

WORKDIR /app

# eerst alleen package files
COPY package.json package-lock.json* ./

RUN npm install

# dan pas rest
COPY . .

RUN npm run build

CMD ["npm", "run", "preview", "--", "--host"]
