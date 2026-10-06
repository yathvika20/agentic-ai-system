import { useState, useRef, useCallback } from "react";

export function useAgentChat(sessionId) {

    const [messages, setMessages] = useState([]);
    const [isStreaming, setIsStreaming] = useState(false);

    const wsRef = useRef(null);

    const sendMessage = useCallback((text) => {

        if (wsRef.current) {
            wsRef.current.close();
        }

        const userMsg = {
            role: "user",
            content: text,
            id: Date.now()
        };

        const botMsg = {
            role: "assistant",
            content: "",
            id: Date.now() + 1,
            streaming: true
        };

        setMessages(prev => [...prev, userMsg, botMsg]);

        setIsStreaming(true);

        wsRef.current = new WebSocket(
            `ws://localhost:8000/api/v1/ws/${sessionId}`
        );

        wsRef.current.onopen = () => {

            console.log("WebSocket Connected");

            wsRef.current.send(text);

        };

        wsRef.current.onmessage = (e) => {

            if (e.data === "[DONE]") {

                setIsStreaming(false);

                setMessages(prev =>
                    prev.map(msg =>
                        msg.id === botMsg.id
                            ? {
                                  ...msg,
                                  streaming: false
                              }
                            : msg
                    )
                );

                wsRef.current.close();

                return;
            }

            setMessages(prev =>
                prev.map(msg =>
                    msg.id === botMsg.id
                        ? {
                              ...msg,
                              content: msg.content + e.data
                          }
                        : msg
                )
            );

        };

        wsRef.current.onerror = (err) => {

            console.error(err);

            setIsStreaming(false);

        };

        wsRef.current.onclose = () => {

            setIsStreaming(false);

        };

    }, [sessionId]);

    return {
        messages,
        sendMessage,
        isStreaming
    };

}