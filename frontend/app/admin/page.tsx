'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import SubscribersList from '@/components/SubscribersList';
import CreateNewsletterForm from '@/components/CreateNewsletterForm';
import FetchTrendsButton from '@/components/FetchTrendsButton';

export default function AdminPage() {
    const router = useRouter();
    const [authorized, setAuthorized] = useState(false);

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
            router.push('/login');
        } else {
            setAuthorized(true);
        }
    }, [router]);

    if (!authorized) return null;

    return (
        <div className="max-w-6xl mx-auto px-6 py-12">
            <div className="flex justify-between items-center mb-8">
                <h1 className="text-3xl font-bold">Admin Dashboard</h1>
                <div className="flex gap-4 items-center">
                    <FetchTrendsButton />
                    <button
                        onClick={() => {
                            localStorage.removeItem('token');
                            router.push('/login');
                        }}
                        className="text-sm text-red-500 hover:underline"
                    >
                        Logout
                    </button>
                </div>
            </div>

            <div className="grid lg:grid-cols-2 gap-8">
                <CreateNewsletterForm />
                <SubscribersList />
            </div>
        </div>
    );
}
