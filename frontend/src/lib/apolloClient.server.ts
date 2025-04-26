import { ApolloClient, HttpLink, InMemoryCache } from "@apollo/client";
import { cache } from "react";

// Wrap the client creation in React cache for automatic deduplication per request
export const getClient = cache(() => {
  return new ApolloClient({
    cache: new InMemoryCache(),
    link: new HttpLink({
      // Use the 'backend' service name for inter-container communication
      // Or use an env var that defaults to this for flexibility
      uri:
        process.env.INTERNAL_GRAPHQL_ENDPOINT || "http://backend:8000/graphql",
      // You can override the fetch implementation here if needed.
      // fetchOptions: { cache: "no-store" }, // Optional: Prevent caching at fetch level
    }),
  });
});
