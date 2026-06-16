'use client';

import { useState } from 'react';
import api from '@/utils/api';
import { Loader2 } from 'lucide-react';

export default function SubscribeForm() {
    const [email, setEmail] = useState('');
    const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');
    const [message, setMessage] = useState('');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setStatus('loading');
        try {
            await api.post('/subscribers/', { email });
            setStatus('success');
            setMessage('Thanks for subscribing! You are on the list.');
            setEmail('');
        } catch (error: any) {
            setStatus('error');
            setMessage(error.response?.data?.detail || 'Something went wrong. Please try again.');
        }
    };

    return (
        <div className="w-full max-w-md mx-auto">
            <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-3 p-2 bg-surface-container-lowest border-2 border-primary-container rounded-2xl glow-yellow transition-all focus-within:ring-2 ring-primary-container/50">
                <input
                    type="email"
                    placeholder="Enter your work email address"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    className="flex-grow bg-transparent border-none focus:outline-none focus:ring-0 px-4 py-3 font-sans text-on-background text-sm"
                    disabled={status === 'loading' || status === 'success'}
                />
                <button
                    type="submit"
                    disabled={status === 'loading' || status === 'success'}
                    className="bg-primary-container text-on-primary-container font-sans text-label-bold font-bold px-8 py-3 rounded-xl hover:bg-primary-fixed transition-all active:scale-95 flex items-center justify-center min-w-[110px]"
                >
                    {status === 'loading' ? <Loader2 className="animate-spin h-4 w-4" /> : 'Join Now'}
                </button>
            </form>
            {message && (
                <p className={`mt-3 text-xs text-center font-medium ${status === 'success' ? 'text-green-600' : 'text-rose-600'}`}>
                    {message}
                </p>
            )}
        </div>
    );
}
