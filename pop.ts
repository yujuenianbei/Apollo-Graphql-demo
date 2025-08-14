// pop.ts - A simple TypeScript module

/**
 * Pops the last element from an array and returns it.
 * @param array The array to pop from
 * @returns The popped element or undefined if the array is empty
 */
export function pop<T>(array: T[]): T | undefined {
  return array.pop();
}

// Example usage:
// const items = [1, 2, 3];
// const lastItem = pop(items);
// console.log(lastItem); // 3
// console.log(items); // [1, 2]