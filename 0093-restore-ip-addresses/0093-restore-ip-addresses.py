class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def backtrack(start, parts):
            if start == len(s) and len(parts) == 4:
                valid_ip = ".".join(parts)
                valid_ips.append(valid_ip)
                return

            if len(parts) >= 4 or start >= len(s):
                return

            for end in range(start + 1, min(start + 4, len(s) + 1)):
                part = s[start:end]
                if part[0] == '0' and len(part) > 1:
                    continue                # avoid leading zeros

                if 0 <= int(part) <= 255:
                    backtrack(end, parts + [part])

        valid_ips = []
        backtrack(0, [])
        return valid_ips