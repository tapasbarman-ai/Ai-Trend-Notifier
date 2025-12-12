'use client';

import { useEffect, useState } from 'react';
import api from '@/utils/api';

interface Subscriber {
    id: number;
    email: string;
    subscribed_at: string;
    is_active: boolean;
}

export default function SubscribersList() {
    const [subscribers, setSubscribers] = useState<Subscriber[]>([]);

    useEffect(() => {
        const fetchSubscribers = async () => {
            try {
                const response = await api.get('/subscribers/');
                setSubscribers(response.data);
            } catch (error) {
                console.error('Failed to fetch subscribers', error);
            }
        };
        fetchSubscribers();
    }, []);

    return (
        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 overflow-hidden">
            <div className="p-6 border-b border-gray-200 dark:border-gray-800">
                <h2 className="text-lg font-bold">Subscribers ({subscribers.length})</h2>
            </div>
            <div className="overflow-x-auto">
                <table className="w-full text-sm text-left">
                    <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-800 dark:text-gray-400">
                        <tr>
                            <th className="px-6 py-3">Email</th>
                            <th className="px-6 py-3">Status</th>
                            <th className="px-6 py-3">Date</th>
                        </tr>
                    </thead>
                    <tbody>
                        {subscribers.map((sub) => (
                            <tr key={sub.id} className="bg-white border-b dark:bg-gray-900 dark:border-gray-700">
                                <td className="px-6 py-4 font-medium">{sub.email}</td>
                                <td className="px-6 py-4">
                                    <span className={`px-2 py-1 rounded-full text-xs ${sub.is_active ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                                        {sub.is_active ? 'Active' : 'Inactive'}
                                    </span>
                                </td>
                                <td className="px-6 py-4">
                                    {new Date(sub.subscribed_at).toLocaleDateString()}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}
