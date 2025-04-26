"use client";
import { ApolloClient, ApolloProvider, InMemoryCache } from "@apollo/client";
import React from "react";

const client = new ApolloClient({
  uri:
    process.env.NEXT_PUBLIC_GRAPHQL_ENDPOINT || "http://localhost:8000/graphql",
  cache: new InMemoryCache(),
});

export default client;

export function ApolloClientProvider({
  children,
}: { children: React.ReactNode }) {
  return React.createElement(ApolloProvider, { client, children });
}
