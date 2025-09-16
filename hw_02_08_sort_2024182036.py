array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227, 
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3, 
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92, 
       83,     100,      94,      40,       5,     458,     364,      26,      64,     635, 
       90,     489,      72,     504,      88,      97,     226,     218,     186,     268, 
]

def sort_bubble(arr):
  print('=' * 60)
  print(f'before: {arr}')
  count = len(arr)
  end = count - 1
  while end > 0:
      last = 1
      for i in range(end):
          if arr[i] > arr[i + 1]:
              arr[i], arr[i + 1] = arr[i + 1], arr[i]
              last = i + 1
      end = last - 1
  print(f'after : {arr}')

def sort_select(arr):
  print('=' * 60)
  print(f'before: {arr}')
  count = len(arr)
  for a in range(count):
      min_value = arr[a]
      min_at = a
      for b in range(a + 1, count):
          if arr[b] < min_value:
              min_value = arr[b]
              min_at = b
      arr[a], arr[min_at] = arr[min_at], arr[a]
  print(f'after : {arr}')

def sort_insert(arr):
  print('=' * 60)
  print(f'before: {arr}')
  count = len(arr)
  for i in range(1, count):
      Hero = arr[i]
      j = i
      while j > 0:
          if arr[j - 1] > Hero:
              arr[j] = arr[j - 1]
              j -= 1
          else:
              break
      arr[j] = Hero
  print(f'after : {arr}')

GAPS = [23, 10, 4, 1]

def next_gap(gap):
    for g in GAPS:
        if gap > g:
            return g
    return 1

def sort_shell(arr):
  print('=' * 60)
  print(f'before: {arr}')
  count = len(arr)
  gap = next_gap(count // 2.5)
  while gap > 1:
      for start in range(gap, count):
          Hero = arr[start]
          i = start
          while i >= gap:
              if arr[i - gap] > Hero:
                  arr[i] = arr[i - gap]
                  i -= gap
              else:
                  break
          arr[i] = Hero
      gap = next_gap(gap)
  print(f'after : {arr}')

def main():
  sort_bubble(array[:])
  sort_insert(array[:])
  sort_select(array[:])
  sort_shell(array[:])

if __name__ == '__main__':
  main()

