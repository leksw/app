import React, { useState } from 'React'
import React, { useState, useEffect } from 'React'


const FopStan = () => {
    const [ isLoading, setIsLoading ] = useState(false)
    const [ data, setData ] = useState([])

    useEffect(() => {
        let didCancel = false
        async function fetchData() {
            !didCancel && setIsLoading(true)
            try {
                const fetcher = await fetch(/some/endpoint)
                const response = await fetcher.json()
                !didCancel && setData(response)
            } catch (error) {
                // Do something with error
            } finally {
                !didCancel && setIsLoading(false)   
            }  
        }
        fetchData()
        return () => { didCancel = true }
    }, [])

    return isLoading ? <div>Loading...</div> : <Breakfast data={data} />
}