-- On Init, custom code
-- VARIABLES

-- Edit this if you want the addon to send messages in /p
aura_env.messager_mode = true
aura_env.raid_channelhealer_cds = { "Divine Hymn", "Tranquility", "Aura Mastery", "Healing Tide Totem" }
aura_env.raid_instahealer_cds = { "Revival", "Spirit Link Totem", "Power Word: Barrier", "Rapture", "Light's Wrath" }
aura_env.raid_cd_msgmode = {
    ["Innervate"] = "PARTY",
    ["Divine Hymn"] = "PARTY",
    ["Tranquility"] = "PARTY",
    ["Aura Mastery"] = "PARTY",
    ["Healing Tide Totem"] = "PARTY",
    ["Revival"] = "PARTY",
    ["Spirit Link Totem"] = "RAID",
    ["Power Word: Barrier"] = "RAID",
    ["Rapture"] = "PARTY",
    ["Light's Wrath"] = "PARTY"
}

aura_env.last_used_cd = ""
